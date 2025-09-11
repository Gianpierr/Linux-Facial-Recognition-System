
import { Routes, Route } from 'react-router'
import Home from './components/Home.tsx'
import './App.css'


function App() {
  // this is where we route our pages too
  return (
    <>
    <Routes>
      <Route path="/" element={<Home />}> </Route>

    </Routes>

    
    {/*
      <NavBar
      content= {
        <Routes>
         <Route path="" element={<Home/>}/>
        </Routes>
     
      }/> */ }
      </>
  )
}

export default App
