import './App.css'
import Home from './pages/Home.jsx'
import Cart from './pages/Cart.jsx'
import Profile from './pages/Profile.jsx'
import Register from './pages/Register.jsx'
import { Routes, Route } from 'react-router-dom'
import NavBar from './components/NavBar.jsx'

function App() {

  return (
    <div>
      <NavBar/>
      <main className='main-content'>
        <Routes>
          <Route path='/' element={<Home />}></Route>
          <Route path='/cart' element={<Cart />}></Route>
          <Route path='/profile' element={<Profile />}></Route>
          <Route path='/register' element={<Register />}></Route>
        </Routes>
      </main>
    </div>
  )
}

export default App
