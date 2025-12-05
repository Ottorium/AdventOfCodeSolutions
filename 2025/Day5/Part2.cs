var parts = File.ReadAllText("../../../input.txt").Split("\n\n");
var ranges = parts[0].Split('\n');

var newRanges = new List<(long, long)>();
foreach (var range in ranges)
    newRanges.Add((long.Parse(range.Split('-')[0]), long.Parse(range.Split('-')[1])));


var isOverlap = true;
while (isOverlap)
{
    isOverlap = false;

    var i = 0;
    while (i < newRanges.Count)
    {
        var range = newRanges[i];
        var j = 0;
        while (j < newRanges.Count)
        {
            var other = newRanges[j];

            if (i == j)
            {
                j++;
                continue;
            }

            if (range.Item1 >= other.Item1 && range.Item1 <= other.Item2 ||
                range.Item2 >= other.Item1 && range.Item2 <= other.Item2)
            {
                var rangeStart = Math.Min(range.Item1, other.Item1);
                var rangeEnd = Math.Max(other.Item2, range.Item2);
                newRanges.Add((rangeStart, rangeEnd));
                newRanges.RemoveAt(i);
                if (i < j)
                    newRanges.RemoveAt(j - 1);
                else
                    newRanges.RemoveAt(j);

                isOverlap = true;
                newRanges.ForEach(i => Console.WriteLine($"{i.Item1}-{i.Item2}"));
                Console.WriteLine();
            }

            if (isOverlap) break;

            j++;
        }

        if (isOverlap) break;

        i++;
    }
}

var sum = 0L;
foreach (var range in newRanges)
    sum += range.Item2 - range.Item1 + 1;

Console.WriteLine(sum);