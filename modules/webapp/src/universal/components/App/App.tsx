import styled from 'styled-components';
import React from 'react';

const StyledApp = styled.div({
});

const App: React.FC<any> = () => {
  return (
    <StyledApp>
      <input type="text" />
      <button type="button">Search (not functioning)</button>
      <div>
        result
      </div>
    </StyledApp>
  );
};

export default App;
