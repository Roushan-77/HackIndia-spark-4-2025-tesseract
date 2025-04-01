import { useNavigate } from "react-router-dom";

const Home2 = () => {
  const navigate = useNavigate();

  const goToNextPage = () => {
    navigate("/next2");
  };

  return (
    <div>
    <div className="card" style={{width: '30rem', height:'28rem'}}>
        
    <div className="card-body">
      <h1 className="card-title">Welcome !</h1>
      <p className="card-text" style={{fontSize:'22px'}}>
        All your information will be private, so there is no login.
        Just choose a nickname and we are good to go.
      </p>
      
    </div>
    {/* <label htmlFor="exampleDataList" className="form"></label> */}
        <input className="form" style={{fontSize:'22px'}} list="datalistOptions" id="exampleDataList" placeholder="Choose a nickname..." />
      <button
      onClick={goToNextPage}
       type="button" className="btn1 btn-light"  style={{fontSize:'12px'}} href="/button" >
        SUBMIT</button>
  </div>   
    </div>
  
  );
};

export default Home2;
