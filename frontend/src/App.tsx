import { HashRouter as Router, Route } from 'react-router-dom';

import './App.css';
import Header from './components/Header';
import NotesListPage from './pages/NotesListPage';
import NotePage from './pages/NotePage';

function App() {
  return (
    <Router>
      <div className='container dark'>
        <div className='app'>
          <Header />
          <Route path='/' element={NotesListPage} />
          <Route path='/note/:id' element={NotePage} />
        </div>
      </div>
    </Router>
  );
}

export default App;
