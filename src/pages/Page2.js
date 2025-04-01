// import React from "react";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
// import { ArrowRight } from "lucide-react";

const Page2 = () => {
    const navigate = useNavigate();
  
    const goToNextPage = () => {
        navigate("/next4");
      };
    
        // return (
        //     <div>
      
        //     </div>
        //   );
        
        
        

// function MultiQuestionQuiz() {
  const questions = [
    {
      question: "1. How often you feel more irritable or frustated than usual?",
      options: ["Almost everyday", "Several times a week", "Rarely", "Never"],
    },
    {
      question: "2. Have you been experiencing physical pain, such as headaches, stomachaches, or muscle tension, without a clear cause?",
      options: ["Yes, very frequently", "Sometimes", "Rarely", "Never"],
    },
    {
      question: "3. How often do you find yourself crying even when there is no clear reason for it?",
      options: ["Yes, very frequently", "Sometimes", "Rarely", "Never"],
    },
    {
      question: "4. How many hours do you sleep regularly ?",
      options: ["Less than 4 hours", "Between 4-6 hours", "Between 7-9 hours", "More than 9 hours"],
    },
     { question: "6. Are you pushing people away, even though you might want to connect with them, because you feel like you don’t deserve their care or attention?",
      options: ["Yes, very frequently", "Sometimes", "Rarely", "Never"],
    },
    {
      question: "7. When you do find yourself laughing or smiling, does it feel forced, or does it feel natural?",
      options: ["Natural", "Forced", "Both", "Don't Know"],
    },
    {
      question: "8. Have you ever looked for ways to escape your feelings, even if that meant risky behaviors, or self-destructive habits?",
      options: ["Sometimes", "Rarely", "Always", "Never"],
    },
  ];

  const [answers, setAnswers] = useState(Array(questions.length).fill(""));

  const handleChange = (index, value) => {
    const newAnswers = [...answers];
    newAnswers[index] = value;
    setAnswers(newAnswers);
  };

  const handleSubmit = () => {
    console.log("Selected Answers:", answers);
    alert("Your answers have been submitted!");
  };

  return (
    
          <div style={{
            width: 1202.74,
            height: 2485.42,
            left: 145.98,
            top: 99,
            position: "absolute",
            // transform: "rotate(26deg)",
            transformOrigin: "top left",
            background:
              "white",
          }}>
      {questions.map((q, index) => (
        <div key={index} style={{width:1200,height:300, fontSize: 16, fontFamily: 'Inter', fontWeight: '500', wordWrap: 'break-word'}}>
          <h3>{q.question}</h3>
          {q.options.map((option, i) => (
            <label key={i} style={{width:1500,height:25, color: '#004C3A', fontSize: 32, fontFamily: 'Inter', fontWeight: '500', wordWrap: 'break-word'}}>
              <input
                type="radio"
                name={`question-${index}`}
                value={option}
                checked={answers[index] === option}
                onChange={(e) => handleChange(index, e.target.value)}
              />
              {option}
            </label>
          ))}
        </div>
      ))}
      <br />
      <button onClick={handleSubmit} style={{left: 110, top: 2400,width: 203, height: 60, position: 'absolute', textAlign: 'center', color: 'blue', fontSize: 32, fontFamily: 'Cairo', fontWeight: '700', wordWrap: 'break-word', textShadow: '0px 4px 4px rgba(110, 108, 108, 0.86)', borderRadius:10,}} disabled={answers.includes("")}>
        SUBMIT
      </button>
      {/* <div>              */}
      <button
      onClick={goToNextPage}
       type="button" className="btn1 btn-light"  style={{left: 1010, top: 2435,width: 203, height: 60, position: 'absolute', textAlign: 'center', color: 'white', fontSize: 32, fontFamily: 'Cairo', fontWeight: '700', wordWrap: 'break-word', textShadow: '0px 4px 4px rgba(61, 58, 58, 0.86)'}} href="/button" >
        NEXT</button>
        {/* </div> */}
    </div>
  );
}

// };
// export default MultiQuestionQuiz;





        export default Page2;