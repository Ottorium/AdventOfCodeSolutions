fn main() {
    let content = include_str!("input.txt");
    let parts = content.split("\n\n").collect::<Vec<&str>>();
    let presents = parts.iter().take(parts.len() - 1);
    let tests = parts.last().unwrap().split('\n').collect::<Vec<&str>>();
    let mut sizes: Vec<u32> = Vec::new();
    for present in &presents {
        let mut count = 0;
        for c in present.chars() {
            if c == '#' {
                count += 1;
            }
        }
        sizes.push(count);
    }

    sizes = presents.map();

    let mut sum = 0;
    for test in tests {
        let parts = test.split(": ").collect::<Vec<&str>>();
        let size_available_vec = parts[0].split("x").collect::<Vec<&str>>();
        let size_available = size_available_vec[0].parse::<u32>().unwrap()
            * size_available_vec[1].parse::<u32>().unwrap();

        let mut piece_count = 0;
        for (i, x) in parts[1].split(" ").enumerate() {
            piece_count += x.parse::<u32>().unwrap() * sizes[i];
        }

        if size_available > ((piece_count as f32 * 1.2) as u32) {
            sum += 1;
        }
    }
    println!("{}", sum);
}
