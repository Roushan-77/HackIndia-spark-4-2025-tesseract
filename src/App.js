import React from 'react';
import Home from "./pages/Home";
import Home2 from './pages/Home2';
import Page1 from './pages/Page1';
import Page2 from './pages/Page2';
import Page3 from './pages/Page3';
import Page3a from './pages/Page3a';
import Page3b from './pages/Page3b';
import Page4 from './pages/Page4';
import Page5 from './pages/Page5';
import Page6 from './pages/Page6';
import Page7 from './pages/Page7';
import './App.css';
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/next" element={<Home2 />} />
        <Route path="/next2" element={<Page1 />} />
        <Route path="/next3" element={<Page2 />} />
        <Route path="/next4" element={<Page3 />} />
        <Route path="/next4a" element={<Page3a />} />
        <Route path="/next4b" element={<Page3b />} />
        <Route path="/next5" element={<Page4 />} />
        <Route path="/next6" element={<Page5 />} />
        <Route path="/next7" element={<Page6 />} />
        <Route path="/next8" element={<Page7 />} />
      </Routes>
    </Router>
  );
}

export default App;
