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
    <GoogleOAuthProvider clientId="
59866668171-pp375fmi3oshu77eouj0lr0s4akfk45v.apps.googleusercontent.com">
      <App />
      </GoogleOAuthProvider>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
