# k-nearest neighbors algorithm (k-NN)

## What is k-NN?

In statistics, the `k-nearest neighbors algorithm (k-NN)` is a non-parametric classification method developed by `Evelyn Fix` and `Joseph Hodges` in `1951` and later expanded by `Thomas Cover`. Used for classification and regression. In both cases, the input includes training models close to the data set. Output depends on whether k-NN is used for classification or regression:

- In the k-NN classification, the output of the class membership. An item is divided by a majority vote of its neighbors, the item is assigned the most common category among its closest neighbors and k. If `k = 1`, then the object is given to the class of that one nearest neighbor.
- In k-NN regression, the output is the property value for the object. This value is the average value of `k` for nearby neighbors.

## Dataset

Dataset used for the model is `“Fish.csv”`. Dataset consists of `159 rows` and `7 columns`.

### Dataset Description

The attributes used in dataset are given bellow:

- Species
- Weight
- Length1
- Length2
- Length3
- Height
- Width

### Independent Attributes

Independent attributes in dataset are:

- Length1
- Length2
- Length3
- Height
- Width

### Dependent Attribute

Dependent attribute in dataset is:

- Weight

### Target Attribute

Target attribute in dataset is:

- Weight

We will predict the weight of fish by using other attributes to train the model.

## Dataset Head

Here is the head of dataset used in the model.

<p align="center">
  <a href="#">
    <img src="https://user-images.githubusercontent.com/93377842/147447741-78c1a544-d82f-4bf9-b284-419e4c21dcf6.png" />
  </a>
</p>

## Dataset Preprocessing

As we don't need `Species` attribute to predict the weight of fish. So, we will drop `Species` attribute. The final dataset is given below:

<p align="center">
  <a href="#">
    <img src="https://user-images.githubusercontent.com/93377842/147448549-59a2fa25-7b05-40b1-9311-99a7428a9e5c.png" />
  </a>
</p>

## Model Training

After preprocessing the dataset, we used preprocessed data for model training. For this purpose, we split up the data and select `30%` of data for test purposes and `70%` of data for model training. We test our model for `k up to 20` to get minimum `Root Mean Square Error (RMSE)`. The `RMSE` for different values of k are given below:

<p align="center">
  <a href="#">
    <img src="https://user-images.githubusercontent.com/93377842/147448904-61fc4298-6147-49c0-80f7-22d14484eb79.png" />
  </a>
</p>

As it is clear from the above figure that RMSE is minimum for `k = 3`.

> **_RMSE value for k = 3 is: 47.21824893415052_**

## Prediction Results

So, we used `k = 3` for the prediction of the weight of fishes. As we get minimum RMSE on 3 which is approximately `47`. The prediction results are given below:

<p align="center">
  <a href="#">
    <img src="https://user-images.githubusercontent.com/93377842/147450636-48747cb8-fc09-4ee5-85f6-ac3c6ba8bfa9.png" />
  </a>
</p>

## References

- Dataset Link: [View Fish Dataset](https://www.kaggle.com/aungpyaeap/fish-market)
- Download Link: [Download Fish Dataset](https://www.kaggle.com/aungpyaeap/fish-market/download)
