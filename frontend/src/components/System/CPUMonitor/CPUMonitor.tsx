import React from 'react';
import './CPUMonitor.css';


export default function CPUMonitor(usage: number = 0) {

    const getColor = (percentage: number) => {
        if (percentage < 50) return '#2ecc71';
        if (percentage > 80) return '#f39c12';
        return '#e74c3c'
    }

    const getStatus = (percentage: number) => {
        if (percentage < 50) return "Normal";
        if (percentage < 80) return "Moderate";
        return "High";
    }


    return(
        <div className="cpu-container">
            <div className="cpu-header">
                <span className="cpu-label"> CPU Usage </span>
                <span className="cpu-value" style={{color: getColor(usage)}}>
                    {usage.toFixed(1)}%
                </span>
            </div>
            <div className="progress-bar"></div>





        </div>


    );
}