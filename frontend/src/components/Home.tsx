import React from 'react';
import Dashboard from './Dashboard/Dashboard.tsx'
import SideBar from './Sidebar/Sidebar.tsx'
import Navigation from './Navigation/Navigation.tsx'
export default function Home() {
    {/* CALL DJANGO API TO GET ALL IMPORTANT INFORMATION DYNAMICALLY LOADED */}
    
    return(
        <main className="grid">
          <Navigation />
          <SideBar />
          <Dashboard />
        </main>
        
    )

}