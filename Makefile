NAME = xdo

SOURCE = 	xdo.c	

CFLAGS += -lX11 -lXtst -lXext

OBJECTS = $(SOURCE:.c=.o)

LIBFT = libft/libft.a

CC = cc

RM = rm -f


%.o: %.c 
	${CC} ${CFLAGS} $ -c $< -o $@
${NAME}: ${OBJECTS}
	${CC} ${CFLAGS} ${OBJECTS} -o ${NAME}

clean:	
	${RM} ${OBJECTS}
fclean:	clean
		${RM} ${NAME}
re:		fclean all
all:	${NAME}
make:	make all

.PHONY: clean fclean re all