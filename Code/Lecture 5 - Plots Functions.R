library(ggplot2)

# 700x400
df.1 = 2^c(1:10)
plot(df.1, type ="l", xlab="", ylab="", xaxt = "n", yaxt="n")

df.2 = exp(c(1:10))
plot(df.2, type ="l", xlab="", ylab="", xaxt = "n", yaxt="n")

df.3 = log10(c(1:10))
plot(df.3, type ="l", xlab="", ylab="", xaxt = "n", yaxt="n")

df.4 = as.data.frame(log10(c(3,5,7,5,3,1,4,7,3)))
names(df.4) = c("x1")
plot(df.4, type ="l", xlab="", ylab="", xaxt = "n", yaxt="n")

ggplot(mtcars, aes(wt, mpg,color=I("black"))) +
  geom_smooth(method = "loess", span = 0.3, se = FALSE) +
  theme_classic()+
  theme(axis.text.x=element_blank(),
        axis.text.y=element_blank(),axis.ticks=element_blank(),
        axis.title.x=element_blank(),
        axis.title.y=element_blank())
