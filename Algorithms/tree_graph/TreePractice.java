
public class TreePractice {

	public static void main(String[] args) {
		TreeNode[] all = new TreeNode[15];
		
		for(int i = 0; i<15; i++){
			TreeNode temp = new TreeNode(i);
			all[i] = temp;
		}
		
		
		for(int i = 0; i<7; i++){
			all[i].left = all[2*i + 1];
			all[i].right = all[2*i + 2];
		}
		TreeNode root = all[0];
		
		System.out.println("\nIn Order");
		inOrderTraversal(root);
		System.out.println("\nPre Order");
		preOrderTraversal(root);
		System.out.println("\nPost Order");
		postOrderTraversal(root);	
		
		
	}

	private static void postOrderTraversal(TreeNode root) {
		if(root == null) return;
		postOrderTraversal(root.left);
		postOrderTraversal(root.right);
		System.out.print(root.val + " ");
	}

	private static void preOrderTraversal(TreeNode root) {
		if(root == null) return;
		System.out.print(root.val + " ");
		preOrderTraversal(root.left);
		preOrderTraversal(root.right);
		
	}

	private static void inOrderTraversal(TreeNode root) {
		if(root==null) return;
		inOrderTraversal(root.left);
		System.out.print(root.val + " ");
		inOrderTraversal(root.right);
		
		
	}
}
