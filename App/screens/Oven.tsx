import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Button } from 'react-native';
import { Image } from 'react-native';

const Oven = ({ navigation }) => {

  const generatePizza = () => {
    console.log(Math.random()*100);
  };

  return (
    <View>
      <Button title="Go to Home" onPress={() => navigation.navigate('Home')} />
      <Button title="Go back" onPress={() => navigation.goBack()} />
      <TouchableOpacity onPress={generatePizza}>
        <Image source={require('../assets/oven_800.jpg')}
        style={{width:300,
        height:300}}/>
      </TouchableOpacity>
    </View>
  );
};

export default Oven;
