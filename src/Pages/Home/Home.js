import React, { useState } from "react";
import './Home.css';
import { Navigate } from "react-router-dom";
export function Home(){
    let [predict,goPredict]=useState(false);
    if (predict){
        return <Navigate to="/PredictAirConditioner" replace={true}/>;
    }
    return (
        <div id="home">
            <h1 className="title">Conserve Energy By Bettering Our Home Homeostasis</h1>
            <div id="menuContent">
         
                <h3 className="subHead">Home Energy Use In The United States</h3>
                <img src='https://www.researchgate.net/publication/290105581/figure/fig1/AS:317029933436928@1452597234237/Illustration-of-the-hourly-energy-consumption-of-different-appliances-per-household.png'/>
                <p className="textBox">Homes and commercial buildings consume 40% of the energy used in the United States. Of the $2,000 the average American spends paying for energy annually, $200 to $400 could be going to waste from drafts, air leaks around openings, and outdated heating and cooling systems </p>  
                <h3 className="subHead">The Goal Of The Website</h3>
                <h5 className="textBox">With The Sustainability Of Our Planet Becoming A Bigger Focus, We Should Strive To Conserve Energy As Much As Possible. <br/> What Better Place To Start Than Our Homes!</h5>
                <p className="textBox">This Website Uses Machine Learning To Help You Easily Calculate The Cooling Load And Heating Load Of Your Home By Feeding It Your Home Measurements</p>
                <p className="textBox">Get An Accurate Prediction Of Your Home's Cooling And Heating Loads So You Can Construct The Most Energy Efficient HVAC System Possible </p>
                <h4 className="subHead">Cooling Load And Heating Load Prediction</h4>
                    <button className="pre"onClick={()=>{goPredict(true)}}>Go Predict</button>
                    </div>
            
            
        </div>
    )
}