import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import HomeScreen from '../screens/HomeScreen';

const Tab = createBottomTabNavigator();

export default function BottomTabNavigator() {
    return (
      <Tab.Navigator
        // tabBarOptions={{
        //   style: { backgroundColor: 'white', height: 60 },
        //   tabStyle: { paddingTop: 10 },
        // }}
      >
        <Tab.Screen name="Oven" component={HomeScreen} />
        <Tab.Screen name="Breed" component={HomeScreen} />
        <Tab.Screen name="My Pizzas" component={HomeScreen} />
        <Tab.Screen name="Market" component={HomeScreen} />
      </Tab.Navigator>
    );
  }