import React from 'react';
import Card from '../Card/Card.tsx';


import '../Card/Card.css'
import './Dashboard.css'

export default function Dashboard() {
   const cardData = [
      {
         title: "Large Featured Card",
         image: "large.url",
         size: "large"
      },

      {
         title: "tall Featured Card",
         image: "tall.url",
         size: "tall"
      },

      {
         title: "wide Featured Card",
         image: "wide.url",
         size: "wide"
      },

   ]


    return(
       <div className="dashboard">
         <div className="card-grid">
            {cardData.map((card, index)=> (
               <Card
                  key={index}
                  title={card.title}
                  image={card.image}
                  size={card.size}>
                  <div> Content for the card </div>
               </Card>
            ))}

         <div className="card-holder">
            <Card
               key="cpu-utilization"
               title="sub-1"
               image="small-image"
               size="small">
               <div> Div 1</div>
            </Card>
            <Card
               key="memory"
               title="sub-2"
               image="small-image"
               size="small">
               <div> Div 2</div>
            </Card>

            <Card
               key="storage"
               title="sub-3"
               image="small-image"
               size="small">
               <div> Div 3</div>
            </Card>

            <Card
               key="least"
               title="sub-4"
               image="small-image"
               size="small">
               <div> Div 4</div>
            </Card>
         </div>
         </div>
      


         
       </div>
    )
}