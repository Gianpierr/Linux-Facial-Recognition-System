import React from 'react';
import Dashboard from '../components/Main/Dashboard/Dashboard.tsx'
import SideBar from '../components/Main/Sidebar/Sidebar.tsx'
import Navigation from '../components/Main/Navigation/Navigation.tsx'
export default function Main() {
    {/* CALL DJANGO API TO GET ALL IMPORTANT INFORMATION DYNAMICALLY LOADED */}
    
    return(
        <main className="grid">
          <Navigation />
          <SideBar />
          <Dashboard />
        </main>
        
    )

}