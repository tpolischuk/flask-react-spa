import React from "react"

class Standard extends React.Component {

  render() {

    let containerStyle = {
        backgroundColor: '#eee',
        boxShadow: '10px 10px 5px -3px rgba(0,0,0,0.1)',
        height: 'auto',
        width: '50%',
        margin: '0 auto',
        padding: '50px',
        marginBottom: '50px'
    }

    return(

      <div className="iksmeContainer" style={containerStyle}>
        <h4>Selected FULL_CODE here</h4>
        <p>Description: Description here</p>
        <label>Education Standard</label>
        <select>
          <option value="standard">STANDARD</option>
        </select>
        <label>Grade Level</label>
        <select>
          <option value="grade-level">Grade Level</option>
        </select>
        <label>Learning Domain</label>
        <select>
          <option value="learning-domain">Learning Domain</option>
        </select>
        <label>Alignment Tag</label>
        <select>
          <option value="full-code">Full Code</option>
        </select>
      </div>
    )
  }

}

export default Standard
