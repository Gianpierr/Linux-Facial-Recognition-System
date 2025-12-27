
import { Routes, Route } from 'react-router'
import Home from './pages/Home.tsx'
import Main from './pages/Main.tsx'


import './App.css'


function App() {
  // this is where we route our pages too
  return (
    <>
    <Routes>
      <Route path="/" element={<Home />}> </Route>
      <Route path="dashboard" element = {<Main/>}></Route>

    </Routes>

   </>
  )
}

export default App