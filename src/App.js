import { BrowserRouter,Routes,Route,Link } from 'react-router-dom';
import React,{useState} from 'react';
import './App.css';
import { Home } from './Pages/Home/Home';
import { PredictAirConditioner } from './Pages/PredictAirConditioner/PredictAirConditioner';

function App() {
  function NavBar(){
    return (
      <div id="headBar">
        <div className='linkBar'>
        <Link className='link' to="/">Home</Link>
        </div>
      </div>
    )
  }
  return (
    <div className="App">
     <BrowserRouter>
     <NavBar/>
     <Routes>
    <Route path="/" element={<Home/>}/>
    <Route path="/PredictAirConditioner" element={<PredictAirConditioner/>}/>
     </Routes>
     </BrowserRouter>
    </div>
  );
}

export default App;
