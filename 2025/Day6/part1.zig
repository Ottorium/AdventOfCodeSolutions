const std = @import("std");
const Allocator = std.mem.Allocator;
const Assignment = struct { u64, u64, u64, u64, u8 };

pub fn main() !void {
    const allocator = std.heap.page_allocator;

    const assignments = try parseInput(allocator);
    var sum: u64 = 0;
    for (assignments.items) |assignment| {
        if (assignment.@"4" == '+') {
            const result = assignment.@"0" + assignment.@"1" + assignment.@"2" + assignment.@"3";
            sum += result;
        } else if (assignment.@"4" == '*') {
            const result = assignment.@"0" * assignment.@"1" * assignment.@"2" * assignment.@"3";
            sum += result;
        }
    }
    std.debug.print("{d}\n", .{sum});
}

pub fn parseInput(allocator: Allocator) !std.ArrayList(Assignment) {
    const fileContents = @embedFile("input.txt");
    var parts = std.mem.splitSequence(u8, fileContents, "\n");
    var rows = try std.ArrayList([]const u8).initCapacity(allocator, 10);
    defer rows.deinit(allocator);
    while (parts.next()) |r| {
        try rows.append(allocator, r);
    }

    var assignments = try std.ArrayList(Assignment).initCapacity(allocator, 100);

    var nums0 = std.mem.splitSequence(u8, rows.items[0], " ");
    var nums1 = std.mem.splitSequence(u8, rows.items[1], " ");
    var nums2 = std.mem.splitSequence(u8, rows.items[2], " ");
    var nums3 = std.mem.splitSequence(u8, rows.items[3], " ");
    var operators = std.mem.splitSequence(u8, rows.items[4], " ");

    var s0 = nums0.next().?;
    var s1 = nums1.next().?;
    var s2 = nums2.next().?;
    var s3 = nums3.next().?;
    var sop = operators.next().?;

    while (true) {
        var trim0 = s0;
        var trim1 = s1;
        var trim2 = s2;
        var trim3 = s3;
        var trim_op = sop;

        while (trim0.len == 0) {
            trim0 = nums0.next().?;
        }
        while (trim1.len == 0) {
            trim1 = nums1.next().?;
        }
        while (trim2.len == 0) {
            trim2 = nums2.next().?;
        }
        while (trim3.len == 0) {
            trim3 = nums3.next().?;
        }
        while (trim_op.len == 0) {
            trim_op = operators.next().?;
        }

        const n0 = try std.fmt.parseInt(u64, trim0, 10);
        const n1 = try std.fmt.parseInt(u64, trim1, 10);
        const n2 = try std.fmt.parseInt(u64, trim2, 10);
        const n3 = try std.fmt.parseInt(u64, trim3, 10);
        const op = trim_op[0];

        try assignments.append(allocator, .{ n0, n1, n2, n3, op });

        s0 = nums0.next() orelse break;
        s1 = nums1.next() orelse break;
        s2 = nums2.next() orelse break;
        s3 = nums3.next() orelse break;
        sop = operators.next() orelse break;
    }

    return assignments;
}
