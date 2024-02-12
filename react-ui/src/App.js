import './App.css';

const ROWS = 17;
const COLS = 17;

function App() {
  const grid = Array.from({ length: ROWS }, (_, rowIndex) => (
    <div key={rowIndex} className={`grid-row ${rowIndex % 2 !== 0 ? 'odd-row' : ''}`}>
      {Array.from({ length: COLS }, (_, colIndex) => (
        <div
          key={colIndex}
          className={`grid-cell ${colIndex % 2 !== 0 ? 'odd-column' : ''}`}
        ></div>
      ))}
    </div>
  ));

  return (
    <div className="App">
      <h1>quoridor</h1>
      <div className="grid-container">{grid}</div>
    </div>
  );
}

export default App;
