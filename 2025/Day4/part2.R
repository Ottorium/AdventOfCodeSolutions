lines <- readLines("./input.txt")
l <- list()
sum <- 0
dirs <- list(list(0, 1), list(0, -1), list(-1, -1), list(-1, 0), list(-1, 1), list(1, -1), list(1, 0), list(1, 1))
removed <- TRUE
while (removed) {
  l <- list()
  for (i in seq_along(lines))  {
    chars <- strsplit(lines[i], "")[[1]]
    for (j in seq_along(chars)) {
      if (chars[j] != "@") {next}
      adj <- 0
      for (k in seq_along(dirs)) {

        newi <- i + dirs[[k]][[1]]
        newj <- j + dirs[[k]][[2]]

        if (length(lines[newi]) == 0) {next}

        newchars <- strsplit(lines[newi], "")[[1]]

        res <- newchars[newj]

        if (length(res) == 0 || is.na(res)) {
          res <- "."
        }

        if (res == "@") {
          adj <- adj + 1
        }

      }

      # print(adj)
      if (adj < 4) {
        l <- append(l, list(list(i, j)))
      }
    }
  }


  removed <- FALSE
  for (p in l) {
    i <- p[[1]]
    j <- p[[2]]
    sum <- sum + 1
    removed <- TRUE
    substr(lines[i], j, j) <- "."
  }
}
cat(sum)
cat("\n")
