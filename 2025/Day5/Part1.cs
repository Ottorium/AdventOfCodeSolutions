var parts = File.ReadAllText("../../../input.txt").Split("\n\n");
var ranges = parts[0].Split('\n');
var ings = parts[1].Split('\n');

var rangesList = new List<(long, long)>();
foreach (var range in ranges)
    rangesList.Add((long.Parse(range.Split('-')[0]), long.Parse(range.Split('-')[1])));
    
    
var sum = 0;

foreach (var id in ings)
{
    if (IngredientIsFresh(rangesList, long.Parse(id)))
    {
        sum += 1;
    }

    bool IngredientIsFresh(List<(long, long)> ranges, long id)
    {
        foreach (var range in ranges)
        {
            if (id >= range.Item1 && id <= range.Item2)
            {
                return true;
            }
        }
        return false;
    }
}
Console.WriteLine(sum);