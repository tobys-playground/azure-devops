# A CI/CD pipeline for creating/recreating an AI Joy Detector

## Background

AI can detect emotions from text, but you need to train it first. A common approach is to feed it a lot of texts with labelled emotions (For example, a sentence like 'I am happy' might be labelled as 'joy'), and it will learn how to associate texts with emotions. The more the data, the better the AI.

The training of AI is usually done manually, but many times, we might need to retrain the AI if 1) we updated its code, or 2) new data is available for the AI to learn. After which, we still have to deploy it for others to use. It is a hassle to keep doing this manually.

As such, to save time and effort, we can automate its training and deployment by using a CI/CD pipeline.

## Project

This CI/CD pipeline will be triggered to automatically train/retrain our AI (A DistilBert model) to detect joyful/neutral sentences when a change has been committed to this repo.
Once the training is done, the AI will be automatically deployed online in a web app.

We will be using Azure (Microsoft's Cloud) extensively for this:

![image001 (2)](https://user-images.githubusercontent.com/81354022/135791434-c50e858a-24a2-43a4-9fb6-eb470fbd535f.jpg)

The web app is available at (Only on 5 Oct): 

https://nusdevopsdemo.azurewebsites.net/

Preview:

![image](https://user-images.githubusercontent.com/81354022/135783256-0c32a79f-b2d0-4b2a-b167-08259092d629.png)

