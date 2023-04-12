import { TextField, Button, Box, Alert, Typography, CircularProgress } from '@mui/material';
import { useEffect, useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { setUserToken } from '../../features/authSlice';
import { getToken, storeToken } from '../../services/LocalStorageService';
import { useLoginUserMutation } from '../../services/userAuthApi';

const UserLogin = () => {
  const [server_error, setServerError] = useState('')
  const navigate = useNavigate();
  const [loginUser, { isLoading }] = useLoginUserMutation()
  const dispatch = useDispatch()
  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new  FormData(e.currentTarget);
    const actualData = {
      username: data.get('username'),
      password: data.get('password'),
    }
    const res = await loginUser(actualData)
    if (res.error) {
      setServerError(res.error.data.detail)
    }
    else if(res.data) {
      storeToken(res.data)
      let { access_token } = getToken()
      dispatch(setUserToken({ access_token: access_token }))
      navigate('/home')
    }
  }
  let { access_token } = getToken()
  useEffect(() => {
    dispatch(setUserToken({ access_token: access_token }))
  }, [access_token, dispatch])


  return <>
    <Box component='form' noValidate sx={{ mt: 1 }} id='login-form' onSubmit={handleSubmit}>
      <TextField margin='normal' required fullWidth id='username' name='username' label='User Name' />
      {server_error ? <Typography style={{ fontSize: 12, color: 'red', paddingLeft: 10 }}>{server_error}</Typography> : ""}
      <TextField margin='normal' required fullWidth id='password' name='password' label='Password' type='password' />
      {/* {server_error ? <Typography style={{ fontSize: 12, color: 'red', paddingLeft: 10 }}>{server_error}</Typography> : ""} */}
      <Box textAlign='center'>
        {isLoading ? <CircularProgress /> : <Button type='submit' variant='contained' sx={{ mt: 3, mb: 2, px: 5 }}>Login</Button>}
      </Box>
      {/* <NavLink to='/sendpasswordresetemail' >Forgot Password ?</NavLink> */}
      {server_error.non_field_errors ? <Alert severity='error'>{server_error.non_field_errors[0]}</Alert> : ''}
    </Box>
  </>;
};

export default UserLogin;