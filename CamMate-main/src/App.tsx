import React, { useEffect, useState } from 'react';
import { Routes, Route, Navigate, useLocation, useNavigate } from 'react-router-dom';

import Loader from './common/Loader';
import PageTitle from './components/PageTitle';
import SignIn from './pages/Authentication/SignIn';
import SignUp from './pages/Authentication/SignUp';
import Calendar from './pages/Calendar';
import Chart from './pages/Chart';
import ECommerce from './pages/Dashboard/ECommerce';
import FormElements from './pages/Form/FormElements';
import FormLayout from './pages/Form/FormLayout';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Tables from './pages/Tables';
import Alerts from './pages/UiElements/Alerts';
import Buttons from './pages/UiElements/Buttons';
import DefaultLayout from './layout/DefaultLayout';
import LiveView from './pages/LiveView';

const ProtectedRoute = ({ children }: { children: JSX.Element }) => {
  const token = localStorage.getItem('token');
  const isLoggedIn = token !== null;
  return isLoggedIn ? children : <Navigate to="/auth/signin" />;
};

const Logout = () => {
  const navigate = useNavigate();

  useEffect(() => {
    localStorage.removeItem('token');
    sessionStorage.removeItem('token');

    navigate('/auth/signin');
  }, [navigate]);

  return <Loader />; 
};

function App() {
  const [loading, setLoading] = useState<boolean>(true);
  const { pathname } = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  useEffect(() => {
    setTimeout(() => setLoading(false), 1000);
  }, []);

  const token = localStorage.getItem('token');
  const isLoggedIn = token !== null;

  if (loading) {
    return <Loader />;
  }

  return (
    <Routes>
      {/* Authentication Routes */}
      <Route
        path="/auth/signin"
        element={isLoggedIn ? <Navigate to="/" /> : <>
          <PageTitle title="Signin" />
          <SignIn />
        </>}
      />
      <Route path="/auth/signup" element={<>
        <PageTitle title="Signup" />
        <SignUp />
      </>} />
      <Route path="/auth/logout" element={<Logout />} />

      {/* Protected Routes */}
      <Route path="/" element={<ProtectedRoute><DefaultLayout /></ProtectedRoute>}>
        <Route index element={<><PageTitle title="Dashboard" /><ECommerce /></>} />
        <Route path="calendar" element={<><PageTitle title="Calendar" /><Calendar /></>} />
        <Route path="profile" element={<><PageTitle title="Profile" /><Profile /></>} />
        <Route path="settings" element={<><PageTitle title="Settings" /><Settings /></>} />
        <Route path="forms/form-elements" element={<><PageTitle title="Form Elements" /><FormElements /></>} />
        <Route path="forms/form-layout" element={<><PageTitle title="Form Layout" /><FormLayout /></>} />
        <Route path="tables" element={<><PageTitle title="Tables" /><Tables /></>} />
        <Route path="chart" element={<><PageTitle title="Chart" /><Chart /></>} />
        <Route path="ui/alerts" element={<><PageTitle title="Alerts" /><Alerts /></>} />
        <Route path="ui/buttons" element={<><PageTitle title="Buttons" /><Buttons /></>} />
        <Route path="liveView" element={<><PageTitle title="Live View" /><LiveView /></>} />
      </Route>
    </Routes>
  );
}

export default App;
