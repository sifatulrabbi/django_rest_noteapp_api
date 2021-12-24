import React from 'react';
import { Link } from 'react-router-dom';
import { ReactComponent as AddIcon } from '../assets/add.svg';

export const AddButton = () => {
  return (
    <Link to='/note/new' className='floating-button'>
      <AddIcon />
    </Link>
  );
};
