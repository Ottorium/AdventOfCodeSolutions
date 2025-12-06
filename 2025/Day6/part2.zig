const std = @import("std");
const Allocator = std.mem.Allocator;
const Assignment = struct { []u8, []u8, []u8, []u8, u8 };

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    var res = try parseInput(allocator);
    defer {
        for (res.rows.items) |row| {
            allocator.free(row);
        }
        res.rows.deinit(allocator);
    }
    const assignments = res.assignments;
    var sum: u64 = 0;
    for (assignments.items) |assignment| {
        const length = assignment.@"0".len;

        if (assignment.@"4" == '+') {
            var inner_sum: u64 = 0;
            for (0..length) |j| {
                var s = try std.ArrayList(u8).initCapacity(allocator, 5);
                defer s.deinit(allocator);
                if (assignment.@"0"[j] != ' ') {
                    try s.append(allocator, assignment.@"0"[j]);
                }

                if (assignment.@"1"[j] != ' ') {
                    try s.append(allocator, assignment.@"1"[j]);
                }

                if (assignment.@"2"[j] != ' ') {
                    try s.append(allocator, assignment.@"2"[j]);
                }

                if (assignment.@"3"[j] != ' ') {
                    try s.append(allocator, assignment.@"3"[j]);
                }

                const result = try std.fmt.parseInt(u64, s.items, 10);
                inner_sum += result;
            }
            sum += inner_sum;
        } else if (assignment.@"4" == '*') {
            var inner_sum: u64 = 1;
            for (0..length) |j| {
                var s = try std.ArrayList(u8).initCapacity(allocator, 5);
                defer s.deinit(allocator);
                if (assignment.@"0"[j] != ' ') {
                    try s.append(allocator, assignment.@"0"[j]);
                }

                if (assignment.@"1"[j] != ' ') {
                    try s.append(allocator, assignment.@"1"[j]);
                }

                if (assignment.@"2"[j] != ' ') {
                    try s.append(allocator, assignment.@"2"[j]);
                }

                if (assignment.@"3"[j] != ' ') {
                    try s.append(allocator, assignment.@"3"[j]);
                }

                const result = try std.fmt.parseInt(u64, s.items, 10);
                inner_sum *= result;
            }
            sum += inner_sum;
        }
    }
    std.debug.print("{d}\n", .{sum});
}

pub fn parseInput(allocator: Allocator) !struct { assignments: std.ArrayList(Assignment), rows: std.ArrayList([]u8) } {
    const fileContents = @embedFile("input.txt");
    var parts = std.mem.splitSequence(u8, fileContents, "\n");
    var rows = try std.ArrayList([]u8).initCapacity(allocator, 10);
    while (parts.next()) |r| {
        const buffer: []u8 = try allocator.alloc(u8, r.len);
        std.mem.copyForwards(u8, buffer, r);
        try rows.append(allocator, buffer);
    }

    var assignments = try std.ArrayList(Assignment).initCapacity(allocator, 100);
    var i: usize = 0;

    while (true) {
        const i_start = i;

        if (i == 0) {
            i += 1;
        }

        while (true) {
            if (i >= rows.items[0].len) {
                break;
            }

            if (std.mem.eql(u8, &[1]u8{rows.items[0][i]}, " ") and std.mem.eql(u8, &[1]u8{rows.items[1][i]}, " ") and std.mem.eql(u8, &[1]u8{rows.items[2][i]}, " ") and std.mem.eql(u8, &[1]u8{rows.items[3][i]}, " ")) {
                break;
            }

            i += 1;
        }

        if (i > rows.items[0].len + 1 or i_start > rows.items[0].len) {
            break;
        }

        const s0 = if (i < rows.items[0].len) rows.items[0][i_start..i] else rows.items[0][i_start..];
        const s1 = if (i < rows.items[0].len) rows.items[1][i_start..i] else rows.items[1][i_start..];
        const s2 = if (i < rows.items[0].len) rows.items[2][i_start..i] else rows.items[2][i_start..];
        const s3 = if (i < rows.items[0].len) rows.items[3][i_start..i] else rows.items[3][i_start..];
        const op = rows.items[4][i_start];

        try assignments.append(allocator, .{ s0, s1, s2, s3, op });

        i += 1;
    }

    return .{
        .assignments = assignments,
        .rows = rows,
    };
}
