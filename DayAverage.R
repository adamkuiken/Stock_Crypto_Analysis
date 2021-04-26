#Adam Kuiken
rm(list = ls())
wd <- setwd('C:/Users/adkui/Desktop/ProjectWithJoe/Stocks/CryptoData/CryptoCSV')
#fp = "Desktop/ProjectWithJoe/Stocks/CryptoData/CryptoCSV"
lis <- list.files(wd)
lis
i = 0
writingLis <- c(length(lis)-1)

mins <- c(50)
maxs <- c(50)
mons <- c(50)
tues <- c(50)
weds <- c(50)
thurs <- c(50)
fris <- c(50)
sats <- c(50)
suns <- c(50)
minIndex <- c(50)
maxIndex <- c(50)
diffs <- c(50)
namez <- c(50)
for(file in 2:length(lis)){
    
    df = read.csv(lis[file],header=TRUE,sep = ",")
    df$Close..
    #Strip commas from close
    df$Close <- as.numeric(gsub(",","",df$Close..))
    df$Close
    ovrAvg <- mean(df$Close)
    ovrAvg
    df$newDate <- as.Date(df$Date,"%Y-%m-%d",optional = FALSE)
    
    df$weekdayz <-weekdays(df$newDate)
    
    #get the close for each of the days of the week 
    Monday <- df[grep("Monday",df$weekdayz),]
    Tuesday <- df[grep("Tuesday",df$weekdayz),]
    Wednesday <- df[grep("Wednesday",df$weekdayz),]
    Thursday <- df[grep("Thursday",df$weekdayz),]
    Friday <- df[grep("Friday",df$weekdayz),]
    Saturday <- df[grep("Saturday",df$weekdayz),]
    Sunday <- df[grep("Sunday",df$weekdayz),]
    
    
     
    averages <- c(mean(as.numeric(Monday$Close), na.rm = TRUE),mean(as.numeric(Tuesday$Close), na.rm = TRUE),mean(as.numeric(Wednesday$Close), na.rm = TRUE),mean(as.numeric(Thursday$Close), na.rm = TRUE),mean(as.numeric(Friday$Close), na.rm = TRUE),mean(as.numeric(Saturday$Close), na.rm = TRUE),mean(as.numeric(Sunday$Close), na.rm = TRUE))
    
    dfAv <- data.frame(averages)
    buy <- min(dfAv)
    sell <- max(dfAv)
    minDex <- which.min(averages)
    maxDex <- which.max(averages)
    
    mins[i] <- buy
    maxs[i] <- sell
    minIndex[i] <- minDex
    maxIndex[i] <- maxDex
    diffs[i] <- sell-buy
    namez[i] <- lis[file]
    writing = paste(lis[file],"\nmin: ",toString(sell)," ",toString(minDex), "\nmax: ",toString(buy)," ",toString(maxDex),"\nOVR AVG: ",toString(ovrAvg),"\nDifference: ",toString(sell-buy),"... \n\n",sep = " ")
    writing
    writingLis[i] = writing
    
    i = i + 1
}
xdf <- data.frame(cbind(namez,mins,maxs,minIndex,maxIndex,diffs))
head(xdf)
write.csv(xdf,file = "0_Averages.csv")
for( j in 0:length(writingLis)-1){
    write(writingLis[i], file = "0_AveragesOutput.txt")
}
print("Done.")

