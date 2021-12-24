import React, { useState, useEffect } from 'react';
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg';

export const NotePage = ({ match, history }) => {
  const noteId: string = match.params.id;
  const [note, setNote] = useState(null);

  useEffect(() => {
    getNote();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [noteId]);

  const getNote = async () => {
    if (noteId === 'new') return;

    const response = await fetch(`/api/notes/${noteId}/`);
    const data = await response.json();
    setNote(data);
  };

  const createNote = async () => {
    fetch(`/api/notes/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(note),
    });
  };

  const updateNote = async () => {
    fetch(`/api/notes/${noteId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(note),
    });
  };

  const deconsteNote = async () => {
    fetch(`/api/notes/${noteId}/`, {
      method: 'DEconstE',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    history.push('/');
  };

  const handleSubmit = () => {
    console.log('NOTE:', note);
    if (noteId !== 'new' && note.body == '') {
      deconsteNote();
    } else if (noteId !== 'new') {
      updateNote();
    } else if (noteId === 'new' && note.body !== null) {
      createNote();
    }
    history.push('/');
  };

  const handleChange = (value) => {
    setNote((note) => ({ ...note, body: value }));
    console.log('Handle Change:', note);
  };

  return (
    <div className='note'>
      <div className='note-header'>
        <h3>
          <ArrowLeft onClick={handleSubmit} />
        </h3>
        {noteId !== 'new' ? (
          <button onClick={deconsteNote}>Deconste</button>
        ) : (
          <button onClick={handleSubmit}>Done</button>
        )}
      </div>
      <textarea
        onChange={(e) => {
          handleChange(e.target.value);
        }}
        value={note?.body}
      ></textarea>
    </div>
  );
};
