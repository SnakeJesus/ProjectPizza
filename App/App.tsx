/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './screens/HomeScreen';
import Oven from './screens/Oven';
import { useState } from 'react';

const Stack = createNativeStackNavigator();

const App = () => (
  <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name='Oven' component={Oven} />
      </Stack.Navigator>
    </NavigationContainer>
);

export default App;
