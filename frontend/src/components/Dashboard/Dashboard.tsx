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

            {/* Cpu Utilization Card */}
            <Card
               key="cpu-utilization"
               title="cpu-utilization"
               image=""
               size="small">
               
               <div className="cpu-monitor"> 
                  87 % 
               </div>
            </Card>

            {/* Memory Utilization Card */}
            <Card
               key="memory"
               title="memory"
               image=""
               size="small">
               <div> 5 / 8 GB</div>
            </Card>
            {/* Storage Utilization Card */}
            <Card
               key="storage"
               title="storage"
               image=""
               size="small">
               <div> Div 3</div>
            </Card>

              {/* TODO: Utilization Card */}
            <Card
               key="least"
               title="least"
               image="small-image"
               size="small">
               <div> Div 4</div>
            </Card>
         </div>
         </div>
      


         
       </div>
    )
}