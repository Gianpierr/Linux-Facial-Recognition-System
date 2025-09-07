
import { Routes, Route } from 'react-router'
import Home from './components/Home.tsx'
import NavBar from './components/navbar/NavBar.tsx'
import './App.css'

function App() {
  // this is where we route our pages too
  return (
    <>
      <NavBar
      content= {
        <Routes>
         <Route path="" element={<Home/>}/>
        </Routes>
     
      }/>
      
     
    </>
  )
}

export default App
