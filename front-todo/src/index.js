import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Provider } from 'react-redux'
import { store } from './app/store'
import {GoogleOAuthProvider} from '@react-oauth/google';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
    <GoogleOAuthProvider clientId={process.env.REACT_APP_clientId}>
      <App />
      </GoogleOAuthProvider>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
