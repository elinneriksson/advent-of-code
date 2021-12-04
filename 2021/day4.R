library(stringr); library(dplyr)
#### Read data ####
day4.input <- read.csv("~/R/advent-of-code/2021/day4-input.txt", 
                       header = FALSE, colClasses = "character")
board_size <- 5 

draw_numbers <- day4.input[1,]
day4.input <- day4.input[-1,"V1"]
boards <- as.data.frame(matrix(ncol = board_size, nrow = length(day4.input)))
for (col in c(1:board_size)){
  boards[,col] <- trimws(str_sub(day4.input,start = (col*3-2), end = (col*3)))
}

# List of separate data frames (boards)
boards.list <- vector(mode = "list", length = nrow(boards)/board_size)
for (board in c(1:length(boards.list))) {
  boards.list[[board]] <- boards[seq((board*board_size-4), (board*board_size)), ]
}

#### Part 1 ####
bingo_fastest <- length(draw_numbers)
for (board in boards.list){
  nr_draws <- 0; bingo <- 0
  marked_numbers <- matrix(0,ncol = board_size, nrow = board_size)
  
  while (bingo == 0) {
    nr_draws <- nr_draws + 1
    draw <- draw_numbers[[nr_draws]]
    marked_numbers <- marked_numbers + (draw == board) 
    
    colsum <- colSums(marked_numbers)
    rowsum <- rowSums(marked_numbers)
    
    if (sum(rowsum == 5) > 0 | sum(colsum == 5) > 0) {
      bingo <- 1
    }
  }
  if (nr_draws < bingo_fastest){
    bingo_fastest <- nr_draws
    board_fastest <- board
  }
}

#### Part 2 ####
bingo_slowest <- 0
for (board in boards.list){
  nr_draws <- 0; bingo <- 0
  marked_numbers <- matrix(0,ncol = board_size, nrow = board_size)
  
  while (bingo == 0) {
    nr_draws <- nr_draws + 1
    draw = draw_numbers[[nr_draws]]
    marked_numbers <- marked_numbers + (draw == board) 
    
    colsum = colSums(marked_numbers)
    rowsum = rowSums(marked_numbers)
    
    if (sum(rowsum == 5) > 0 | sum(colsum == 5) > 0) {
      bingo = 1
    }
  }
  if (nr_draws > bingo_slowest){
    bingo_slowest <- nr_draws
    board_slowest <- board 
  }
}

#### Results #### 
calculate_result <- function(board, nr_draws, draw_numbers) {
  bingo_list <- as.numeric(as.matrix(board))
  number_list <- as.numeric(as.matrix(draw_numbers[1:nr_draws]))
  remove_numbers <- bingo_list[which(bingo_list %in% number_list)]
  
  result <- (sum(bingo_list)-sum(remove_numbers)) * as.numeric(draw_numbers[[nr_draws]])
  return(result)
}

calculate_result(board_fastest,bingo_fastest,draw_numbers)
calculate_result(board_slowest,bingo_slowest,draw_numbers)