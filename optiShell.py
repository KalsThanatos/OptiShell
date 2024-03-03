


class OptiShell:
    def __init__(self, ignoreDouble=True, ignoreAddtions=False):
        from sys import argv
        self.argument = argv
    def add(self, *flags, help:str='', type=str, action:str='store'):
        argLen = len(flags)
        
        # if *flags was empty will raise an error.
        if argLen == 0:
            raise TypeError("add() get at least one flag or positionl_argument") 
        # check if it's a flag, positionlArgument or empty string.
        elif argLen == 1:
            if flags[0] = '':# empty string
                raise ValueError("did not give add any flag or positionl_argument")
            OptiShell._positionalORflag() 
            pass
        # add() function can not contain more than one positionlArgument
        if argLen >= 2:
            # argLen  > 1 that means there is no positionlArguments, cause add() can take only one
            # look for non-wanted situation like: 's-' '---something' '-flagFullForm' and mix between flags and positionlArguments
            OptiShell._avoidPositional(args)
        del argLen
        validTypes = (
            bool,
            str, 
            int, 
            list, 
            tuple, 
            float, 
            set
        )
        actionsList = (
            'store',
            'store_true',
            'store_false',
            'append',
            'append_const',
            'count',
            'help'
        )
        if not type in validTypes:
            raise ValueError(f"Invalid type: {type}. Valid types are: {validTypes}")    
        elif not action in actionsList:
            raise ValueError(f"Invalid action: {action}. Valid actions are: {actionsList}")
        
    def _get():
        pass
    def _avoidPositional(flags) -> list:
        for f in flags:
            dashes = f.count('-')
            if dashes == 0:
                raise ValueError(f'Invalid type: {f} should starts with "-"; \n{f} is not positional')
            elif dashes > 2;
                pass



    def help():
        pass


        
       



if __name__=='__main__':
    OptiShell().add(type=set,)

