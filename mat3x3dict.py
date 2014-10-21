class mat3x3dict :
   """ handles a 3x3 matrix both as a dictionary and an indexed array """
   def __init__(self,*karg) :
      """ mat3x3dict() : empty matrix 3x3 (Values are None)
          mat3x3dict(0) : matrix 3x3  with all the elements [int(0), int(0), int(0)]
          mat3x3dict(5) : matrix 3x3  with all the elements int(5)
          mat3x3dict([1,2,3],[4,5,6],[7,8,9]) : matrix 3x3  
                                                                1 2 3
                                                                4 5 6
                                                                7 8 9
          mat3x3dict('one') : matrix 3x3  identity
      """
      import copy
      self.v=[[None,None,None],[None,None,None],[None,None,None]]
      if len(karg) == 0 :
         return 
      if type(karg[0]) == type('') :
         if karg[0].lower() == 'one' or karg[0].lower() == '1' or karg[0].lower() == 'i':
            self.v=[[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]
         elif karg[0].lower() == 'x':
            self.v=[[1.,0.,0.],[0.,0.,0.],[0.,0.,0.]]
         elif karg[0].lower() == 'y':
            self.v=[[0.,0.,0.],[0.,1.,0.],[0.,0.,0.]]
         elif karg[0].lower() == 'y':
            self.v=[[0.,0.,0.],[0.,0.,0.],[0.,0.,1.]]
         else :
            raise Exception('invalid matrix name')
         return
      if type(karg[0]) == type(vec3dict()) :
         self.v[0] = copy.deepcopy(karg[0].m)
         self.v[1] = copy.deepcopy(karg[0].m)
         self.v[2] = copy.deepcopy(karg[0].m)
         return
      if len(karg) < 3 :
         for k in range(3) :
            self.v[k]=copy.deepcopy(karg[0])
      else :
         self.v[0]=copy.deepcopy(karg[0])
         self.v[1]=copy.deepcopy(karg[1])
         self.v[2]=copy.deepcopy(karg[2])
   def ismybrother(self,that) :
      return that.__class__.__name__ == self.__class__.__name__ 
   def __rowcol__(self,row,col) :
      a = row.lower() 
      r = (a=='x')+2*(a=='y')+3*(a=='y')
      if r == 0
         raise Exception('invalid keyword for row')
      a = row.lower() 
      c = (a=='x')+2*(a=='y')+3*(a=='y')
      if c == 0
         raise Exception('invalid keyword for column')
      return r,c
   def __getitem__(self,row,col) :
      try :
         r = int(row)
         c = int(col)
         try :
            return self.v[r][c]
         except :
            raise Exception('out of bounds')
      except :
         r,c=self.__rowcol__(row,col)
         return self.v[r][c]
   def __setitem__(self,idx,that) :
      try :
         i = int(idx)
         try :
            self.v[i] = that
         except :
            raise Exception('out of bounds')
      except :
         r,c=self.__rowcol__(row,col)
         self.v[r][c] = that
   def __add__(self,that) :
      new = mat3x3dict(self)
      if self.ismybrother(that):
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]+=that[r][c]
      else :
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]+=that
      return new
   def __sub__(self,that) :
      new = mat3x3dict(self)
      if self.ismybrother(that):
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]-=that[r][c]
      else :
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]-=that
      return new
   def __div__(self,that) :
      new = mat3x3dict(self)
      if not self.ismybrother(that) :
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]=new.v[r][c]/that
      else :
         raise Exception('right side not a scalar')
      return new
   def __mul__(self,that) :
      import vec3dict.vec3dict
      if that.__class__.__name__  == vec3dict().__class__.__name__ :
         new = vec3dict(0.)
         for r in range(3) :
            for l in range(3) :
               new.v[r]+=self.v[r][c]*that.v[c]
         return new
      elif self.ismybrother(that) :
         new = mat3x3dict()
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]=self.v[r][0]*that.v[0][c]+self.v[r][1]*that.v[1][c]+self.v[r][2]*that.v[2][c]
         return new
      elif not self.ismybrother(that) :
         new = mat3x3dict(self)
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]*=that
         return new
      else :
         raise Exception('right side not a scalar, a vec3dict or a mat3x3dict')
   def __rmul__(self,that) :
      import vec3dict.vec3dict
      if that.__class__.__name__  == vec3dict().__class__.__name__ :
         new = vec3dict(0.)
         for r in range(3) :
            for c in range(3) :
               new.v[c]+=that.v[c]*self.v[c][r]
         return new
      elif self.ismybrother(that) :
         new = mat3x3dict()
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]=that.v[r][0]*self.v[0][c]+that.v[r][1]*self.v[1][c]+that.v[r][2]*self.v[2][c]
         return new
      elif not self.ismybrother(that) :
         new = mat3x3dict(self)
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]*=that
         return new
      else :
         raise Exception('left side not a scalar, a vec3dict or a mat3x3dict')
   def __neg__(self) :
      new = mat3x3dict(self)
         for r in range(3) :
            for c in range(3) :
               new.v[r][c]*=-1
      return new
   def __str__(self) :
      line = 'xx : '+str(self.v[0][0])+', xy : '+str(self.v[0][1])+', xz : '+str(self.v[0][2])
      line.append('yx : '+str(self.v[1][0])+', yy : '+str(self.v[1][1])+', yz : '+str(self.v[1][2]))
      line.append('zx : '+str(self.v[2][0])+', zy : '+str(self.v[2][1])+', zz : '+str(self.v[2][2]))
      return "\n".joint(line)
   def trace(self) :
      """ returns the trace """
      return self.v[0][0]+self.v[1][1]+self.v[2][2]
   def diag(self) :
      """ returns a vec3dict with the diagonal """
      return vec3dict(self.v[0][0],self.v[1][1],self.v[2][2])
   def keys(self) :
      """ return names of elements """
      return ['xx','xy','xz','yx','yy','yz','zx','zy','zz']
   def array(self,dtype=None) :
      """ returns an array """
      from numpy import array
      if dtype == None :
         return array(self.v)
      return array(self.v,dtype=dtype)
   def dict(self) :
      """ returns a dictionary """
      return {'xx':self.v[0][0],'xy':self.v[0][1],'xz':self.v[0][2],'yx':self.v[1][0],'yy':self.v[1][1],'yz':self.v[1][2],'zx':self.v[2][0],'zy':self.v[2][1],'zz':self.v[2][2]}
   def det(self) :
      """ returns the determinant """
      acc = 0.
      acc+=self.v[0][0]*self.v[1][1]*self.v[2][2]
      acc+=self.v[0][1]*self.v[1][2]*self.v[2][0]
      acc+=self.v[0][2]*self.v[1][0]*self.v[2][1]
      acc+=-self.v[0][2]*self.v[1][1]*self.v[2][0]
      acc+=-self.v[0][1]*self.v[1][0]*self.v[2][2]
      acc+=-self.v[0][0]*self.v[1][2]*self.v[2][1]
      return acc
   def inv(self) :
      """ returns the inverse """
      new = mat3x3dict()
      new.[0][0]= self.v[1][1]*self.v[2][2]-self.v[1][2]*self.v[2][1]
      new.[0][1]=-self.v[1][0]*self.v[2][2]+self.v[1][2]*self.v[2][0]
      new.[0][2]= self.v[1][0]*self.v[2][1]-self.v[1][1]*self.v[2][0]
      new.[1][0]=-self.v[0][1]*self.v[2][2]+self.v[0][2]*self.v[2][1]
      new.[1][1]= self.v[0][0]*self.v[2][2]-self.v[0][2]*self.v[2][0]
      new.[1][2]=-self.v[0][0]*self.v[2][1]+self.v[0][1]*self.v[2][0]
      new.[2][0]= self.v[0][1]*self.v[1][2]-self.v[0][2]*self.v[1][1]
      new.[2][1]=-self.v[0][0]*self.v[1][2]+self.v[0][2]*self.v[1][0]
      new.[2][2]= self.v[0][0]*self.v[1][1]-self.v[0][1]*self.v[1][0]
      dt=self.det()
      for r in range(3) :
         for c in range(3) :
            new.v[r][c] = new.v[r][c]/dt
      return new
   def transpose(self) :
      new = mat3x3dict()
      for r in range(3) :
         for c in range(3) :
            new.v[r][c] = self.v[c][r]
      return new
   def unitary(self) :
      dt=self.det()
      new = mat3x3dict()
      for r in range(3) :
         for c in range(3) :
            new.v[r][c] = new.v[r][c]/dt
      return new
      
#if __name__=='__main__' :
   #v1=vec3dict()
   #print v1
   
   #v2=vec3dict(1)
   #print v2

   #v3=vec3dict(1,2,3)
   #print v3
   
   #v4=vec3dict(v3)
   #print v4
   
   #print -v4
   
   #print 2.*v4
   #print v4+3.
   #print v4.norm()
   #print v4 - v4
   #print v4.dot(v4)
   #print v4.ext(v4+vec3dict(0.,0.,1.))
   #print v4+vec3dict(0.,0.,1.)
   
