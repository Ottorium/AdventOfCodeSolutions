package main

import (
	"fmt"
	"os"
	s "strings"
)

func must[T any](val T, err error) T {
	if err != nil {
		panic(err)
	}
	return val
}

func contains(slice []string, element string) bool {
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

type Device = struct {
	name    string
	devices []string
}

func main() {
	var data = string(must(os.ReadFile("input.txt")))
	var devices []Device
	var youDevice Device
	for _, line := range s.Split(data, "\n") {
		parts := s.Split(line, ": ")
		deviceName := parts[0]
		others := s.Split(parts[1], " ")
		devices = append(devices, Device{deviceName, others})
		if deviceName == "you" {
			youDevice = Device{deviceName, others}
		}
	}

	sum := getTotalPaths(youDevice, []string{}, devices)
	fmt.Println(sum)
}

func getTotalPaths(device Device, seen []string, devices []Device) int {
	if contains(seen, device.name) {
		return 0
	}

	seen = append(seen, device.name)

	sum := 0
	for _, other := range device.devices {
		if other == "out" {
			sum += 1
			continue
		}

		otherDevice := must(findDevice(devices, other))
		sum += getTotalPaths(otherDevice, seen, devices)
	}
	return sum
}
