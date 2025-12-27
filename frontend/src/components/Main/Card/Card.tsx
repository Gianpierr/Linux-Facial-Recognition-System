import React from 'react';

/* Creating a type for the props and children elements that will be passed */
interface CardProps {
    children: React.ReactNode;
    className ?: string;
    key: string;
    title: string;
    image: string;
    size: string;

}

export default function Card( { children, title, image, size = "normal", className = ""}: CardProps) {
    return(
        
            <div className={`card ${size} ${className}`}>
                { image && (
                    <div className="card-image">
                        <img></img>
                    </div>
                )}
                <div className="card-content">
                    <h3 className="card-title">{title}</h3>
                    {children}

                </div>
            </div>
    


    );
}


