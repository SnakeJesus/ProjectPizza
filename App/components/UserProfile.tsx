import React, { useState } from 'react';
import { View, Text, TextInput, Image, TouchableOpacity } from 'react-native';

const UserProfile = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = () => {
    // code to submit the form data to the server
  };

  return (
    <View>
      <TextInput
        value={username}
        onChangeText={text => setUsername(text)}
        placeholder="Username"
      />
      <TextInput
        value={email}
        onChangeText={text => setEmail(text)}
        placeholder="Email"
      />
      <TextInput
        value={password}
        onChangeText={text => setPassword(text)}
        placeholder="Password"
        secureTextEntry={true}
      />
      <TouchableOpacity onPress={handleSubmit}>
        <Text>Submit</Text>
      </TouchableOpacity>
    </View>
  );
};

export default UserProfile;