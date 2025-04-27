function MyButton() {
  return (
    <button>Select sources</button>
  );
}

export default function Home() {
  return (
    <div className="App">
      <div className="App-header">
        <h1>Frame Generator</h1>
      </div>
      <div className="App-body">
        <div>This tool generates frames from a single or multiple video sources over a specified interval.</div>
        <MyButton />
      </div>
    </div>
  );
}
