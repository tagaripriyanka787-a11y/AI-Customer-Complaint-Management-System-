import "./App.css";
import ComplaintForm from "./components/ComplaintForm";
import ComplaintList from "./components/ComplaintList";

function App() {
  return (
    <div className="App">
      <h1>AI Customer Complaint Management System</h1>

      <ComplaintForm />

      <hr />

      <ComplaintList />
    </div>
  );
}

export default App;
