package main

import (
	"fmt"
	"os"
	"strconv"
	s "strings"
)

func must[T any](val T, err error) T {
	if err != nil {
		panic(err)
	}
	return val
}

func contains[T comparable](slice []T, element T) bool {
	for _, v := range slice {
		if v == element {
			return true
		}
	}
	return false
}

func findDevice(slice []Device, element string) (Device, error) {
	for _, v := range slice {
		if v.name == element {
			return v, nil
		}
	}
	return Device{"", []string{}}, fmt.Errorf("device %s not found", element)
}

type Device struct {
	name    string
	devices []string
}

func (d Device) ToString() string {
	return d.name
}

func main() {
	var data = string(must(os.ReadFile("input.txt")))
	var devices []Device
	var startDevice Device
	for _, line := range s.Split(data, "\n") {
		parts := s.Split(line, ": ")
		deviceName := parts[0]
		others := s.Split(parts[1], " ")
		devices = append(devices, Device{deviceName, others})
		if deviceName == "svr" {
			startDevice = Device{deviceName, others}
		}
	}

	sum := getTotalPaths(startDevice, []string{}, devices, false, false)
	fmt.Println(sum)
}

var resMap = make(map[string]int)

func getTotalPaths(device Device, seen []string, devices []Device, containsDac bool, containsFft bool) int {
	input := "" + device.ToString() + strconv.FormatBool(containsDac) + strconv.FormatBool(containsFft)

	res, cont := resMap[input]
	if cont {
		return res
	}

	if contains(seen, device.name) {
		return 0
	}

	if device.name == "dac" {
		containsDac = true
	}

	if device.name == "fft" {
		containsFft = true
	}

	seen = append(seen, device.name)

	sum := 0
	for _, other := range device.devices {
		if other == "out" {
			if containsDac && containsFft {
				sum += 1
			}
			continue
		}

		otherDevice := must(findDevice(devices, other))
		sum += getTotalPaths(otherDevice, seen, devices, containsDac, containsFft)
	}
	resMap[input] = sum
	return sum
}
