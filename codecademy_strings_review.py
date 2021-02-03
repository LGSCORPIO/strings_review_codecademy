#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:18:18 2021

@author: lilygoodyersait
"""

def username_generator(first_name, last_name):
    username = first_name[:3] + last_name[:4]
    return username
 

username_generator("bo", "sim")

def password_generator(username):
  password=""
  password = username[-1] +username[0:-1]
  return password




def password_generator(username):
  password=""
  for i in range(0,len(username)-1):
     password +=username[i]
  password = username[-1] + password
  return password


password_generator("Gales")
