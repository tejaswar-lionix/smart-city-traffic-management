import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
export default function App(){
  return <BrowserRouter>
    <nav className='p-4 bg-slate-900 text-white flex gap-4'>
      <Link to='/'>Dashboard</Link>
      {["traffic_signals","intersections","sensors","vehicles","incidents","congestion","parking","public_transit"].map(m=><Link key={m} to={'/'+m}>{m}</Link>)}
    </nav>
    <Routes><Route path='/' element={<div className='p-8'>Smart City Traffic Management Platform — 500k LOC</div>}/></Routes>
  </BrowserRouter>
}
