library(tidyr)
day5.input <- read.table("~/R/advent-of-code/2021/day5-input.txt", 
                         comment.char="", stringsAsFactors=FALSE)

data <- separate(separate(day5.input,sep = ",", col = 3, into = c("x2","y2")),
                 sep = ",", col = 1, into = c("x1","y1"))[,-c(3)]
data <- as.data.frame(as.matrix(sapply(data, as.numeric)))

#### Part 1 and 2 #### 
marked_points = c()
for (row in c(1:nrow(data))){
  # If- only in part 1 
  #if (data[row,"x1"] == data[row,"x2"] | data[row,"y1"] == data[row,"y2"])
    marked_points = c(marked_points, 
             paste0(as.character(seq(data[row,"x1"],(data[row,"x2"]))),
                    ",",
                    as.character(seq(data[row,"y1"],(data[row,"y2"])))))

}
result = length(unique(marked_points[which(duplicated(marked_points))]))



