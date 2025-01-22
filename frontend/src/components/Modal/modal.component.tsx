import React from 'react';

export const useModal = ({ children }: React.PropsWithChildren) => {
  const [isOpen, setIsOpen] = React.useState(false);

  const toggleModal = () => setIsOpen(!isOpen);

  const closeModal = () => setIsOpen(false);

  return {
    isOpen,
    toggleModal,
    component: (<>
      {isOpen ?
        <>
          <div className="backdrop" onClick={closeModal} ></div>
          <div className="modal">
            {children}
          </div>
        </> : null}
    </>)
  };
};