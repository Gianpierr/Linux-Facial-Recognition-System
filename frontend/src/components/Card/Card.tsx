import React from 'react';

/* Creating a type for the props and children elements that will be passed */
interface CardProps {
    children: React.ReactNode;
    className ?: string;
}

export default function Card( {children, className = ""}: CardProps) {
    return(
        <div className={`modern-card ${className}`}>
            {children}
        </div>

    );
}


