# Minecraft Map Converter

## Introduction

An old project from 2019 I rediscovered, It was an attempt to show how images were distorted 
when you converted then into a mincraft map colour pallet. However, it was one my first big projects and it really shows.

It's terribly commented, extremely obtuse, and missing many of the techniques I would have used today. Also it's using 8 spaces as indents... so there's that. 

## Why is RGB stored as a single array?

One the things I was intrested in doing with project was using a techinque I'd heard used in Ultimate Doom(1996) of using an offset instead of multiple arrays. The RGB values are stored in a single array as [R1,R2,R3,B1,B2,B3,G1,G2,G3], so in order get the colour of 1 you'd have to refference 3 seperate points. This was terrible hard to develop for and didn't even help performance.


