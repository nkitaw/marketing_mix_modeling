library(tidyverse)
install.packages("corrplot")
install.packages("gplots")
library(corrplot)
library(gplots)

##Case Study

#######Data Cleaning

#Dropping Date Variable - As a first pass we wont be considering time series/seasonality

input_data_nodate <- select(input_data, -c(month) )

#Distribution of variables
sales_dist_plot <- ggplot(data = input_data_nodate, aes(x=sales)) + geom_density(alpha = .5)
TV_dist_plot <- ggplot(data = input_data_nodate, aes(x=TV)) + geom_density(alpha = .5)
Digital_dist_plot <- ggplot(data = input_data_nodate, aes(x=Digital)) + geom_density(alpha = .5)
social_dist_plot <- ggplot(data = input_data_nodate, aes(x=Social)) + geom_density(alpha = .5)

#Distribution of social is right skewed, might benefit from a cube root transformation

cuberoot_social_dist_plot <- ggplot(data = (input_data_nodate) ^ (1/3), aes(x=Social)) + geom_density(alpha = .5)


#######Checking for general correlations and multicollinearity

corrplot.mixed(corr = cor(input_data_nodate, use = "complete.obs"),
               upper = "ellipse", tl.pos = "lt",
               upper.col = colorpanel(50, "red", "gray60", "blue4"))


# Multicollinearity Takeaway: The correlation between TV, Digital, and Social are all relatively not too high, 
#Digital and Social correlation is 35  which kind of makes sense as digital and social are somewhat related

# Genearl correlation Takeaway: Seems like TV and Sales have the strongest correlation (.78), 
#while Digital and sales also has (.58), and the least strongest correlation is between Social and Sales (.23)


#########Multiple Linear Regression Model

# Regression modeling with all the independent variables
model_1 <- lm(sales ~ ., data = input_data_nodate)
summary(model_1)

#Model Takeaway: Based on this first model Tv and Digital are significant variables when it comes to predicting
# Sales but Social is not. As far as effect size, Digital seems to be superior to TV in causing higher sales

#Analyzing normality of the residuals

input <- model_1[["residuals"]] %>% as_tibble()

residual_dist_plot <- ggplot(data = input, aes(x=value)) + geom_density(alpha = .5)

#takeaway: non normal residuals


#Model 2 - 
model_2 <- lm(sales ~ TV + Digital + I(Social ^ (1/3)), data = input_data_nodate)
summary(model_2)


#Analyzing normality of the residuals

input_2 <- model_2[["residuals"]] %>% as_tibble()

residual_dist_plot_2 <- ggplot(data = input_2, aes(x=value)) + geom_density(alpha = .5)

#takeaway non normal residuals


#Model 3 - No Social
model_3 <- lm(sales ~ TV + Digital, data = input_data_nodate)
summary(model_3)

#Analyzing normality of the residuals

input_3 <- model_3[["residuals"]] %>% as_tibble()

residual_dist_plot_3 <- ggplot(data = input_3, aes(x=value)) + geom_density(alpha = .5)





### Question 2 - Visualization

#Changing date field from character to date format
input_final$Date <- as.Date(input_final$Date, "%m/%d/%Y")

viz_input <- input_final %>% 
  select(Date, TV, Digital, Social, sales) %>%
  gather(key = "variable", value = "value", -Date)

all_channels_viz <- ggplot(viz_input, aes(x = Date, y = value)) + 
  geom_line(aes(color = variable, linetype = variable)) +
  labs( title = "Marketing Spend and Sales over Time", y = "Marketing Spend/ Sales")

multiple_plots <- ggplot(viz_input, aes(x = Date, y = value)) + 
  geom_line(aes(color = variable, linetype = variable)) + facet_grid(vars(variable)) +
  labs( title = "Marketing Spend and Sales over Time", y = "Marketing Spend/ Sales")
